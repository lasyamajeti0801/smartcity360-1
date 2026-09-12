"""
SmartCity360 - Comprehensive Realistic Municipal Seed Data Loader
Seeds initial departments, civic service categories, services, role definitions,
sample facilities, complaint categories, and labeled demo infrastructure.
"""

import asyncio
import sys
from pathlib import Path
from datetime import datetime, timezone, timedelta

# Ensure repo root is in python path
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

from sqlalchemy import select
from backend.app.core.database import AsyncSessionLocal, init_db
from backend.app.core.security import get_password_hash, ROLE_CITIZEN, ROLE_CITY_ADMIN, ROLE_DEPT_STAFF, ROLE_FIELD_STAFF, ROLE_EMERGENCY_OPERATOR, ROLE_SUPERVISOR
from backend.app.models.user import User, Role, Permission, CitizenProfile, DepartmentStaff
from backend.app.models.department import Department, ServiceCategory, MunicipalService
from backend.app.models.complaint import ComplaintCategory, Complaint, ComplaintStatusHistory
from backend.app.models.emergency import EmergencyIncident, EmergencyResponseTeam, Facility
from backend.app.models.infrastructure import InfrastructureAsset, StreetlightAsset, WaterAsset, WasteZone
from backend.app.models.mobility import TrafficIncident, ParkingLocation
from backend.app.models.engagement import Announcement, CityEvent

async def seed_data():
    await init_db()
    async with AsyncSessionLocal() as db:
        # Check if already seeded
        existing_dept = (await db.execute(select(Department))).scalars().first()
        if existing_dept:
            print("[INFO] Database already contains records. Skipping seed.")
            return

        print("[INFO] Seeding SmartCity360 with realistic municipal dataset...")

        # 1. Seed Roles
        roles = {
            ROLE_CITIZEN: Role(name=ROLE_CITIZEN, description="Urban citizen accessing civic self-service portal"),
            ROLE_DEPT_STAFF: Role(name=ROLE_DEPT_STAFF, description="Municipal department officer and ticket reviewer"),
            ROLE_FIELD_STAFF: Role(name=ROLE_FIELD_STAFF, description="Field technician executing civic work orders"),
            ROLE_SUPERVISOR: Role(name=ROLE_SUPERVISOR, description="Department supervisor approving field resolutions"),
            ROLE_EMERGENCY_OPERATOR: Role(name=ROLE_EMERGENCY_OPERATOR, description="911/Emergency triage dispatcher"),
            ROLE_CITY_ADMIN: Role(name=ROLE_CITY_ADMIN, description="City Executive Director and System Administrator")
        }
        for r in roles.values():
            db.add(r)
        await db.flush()

        # 2. Seed Departments
        departments = [
            Department(
                code="ROADS",
                name="Roads & Public Infrastructure Department",
                description="Responsible for urban arterial roads, bridges, drainage maintenance, and pothole remediation.",
                contact_email="roads@smartcity360.local",
                contact_phone="+1-555-019-7001",
                head_official="Commissioner Arthur Vance"
            ),
            Department(
                code="SANITATION",
                name="Solid Waste & Sanitation Department",
                description="Manages municipal solid waste collection, recycling programs, and street sweeping operations.",
                contact_email="sanitation@smartcity360.local",
                contact_phone="+1-555-019-7002",
                head_official="Director Elena Rostova"
            ),
            Department(
                code="WATER",
                name="Water Supply & Sewerage Board",
                description="Ensures clean municipal drinking water supply, pipeline integrity, and sewage network operations.",
                contact_email="water@smartcity360.local",
                contact_phone="+1-555-019-7003",
                head_official="Chief Engineer Marcus Sterling"
            ),
            Department(
                code="ELECTRICAL",
                name="Public Lighting & Electrical Utilities",
                description="Maintains streetlights, smart lighting poles, traffic signal grids, and municipal energy efficiency.",
                contact_email="electrical@smartcity360.local",
                contact_phone="+1-555-019-7004",
                head_official="Director Priya Sharma"
            ),
            Department(
                code="EMERGENCY",
                name="Emergency Response & Disaster Management",
                description="Coordinates fire rescue squads, paramedics, traffic incident management, and severe weather response.",
                contact_email="emergency@smartcity360.local",
                contact_phone="+1-555-019-7000",
                head_official="Chief Dispatcher David Chen"
            )
        ]
        dept_map = {}
        for d in departments:
            db.add(d)
            await db.flush()
            dept_map[d.code] = d

        # 3. Seed Complaint Categories
        categories = [
            ComplaintCategory(
                code="POTHOLE",
                name="Pothole & Asphalt Damage",
                default_department_code="ROADS",
                default_sla_hours=48,
                icon_name="Hammer",
                description="Road surface depressions, asphalt cracking, or damaged road shoulders endangering motorists."
            ),
            ComplaintCategory(
                code="GARBAGE",
                name="Overflowing Garbage & Illegal Dumping",
                default_department_code="SANITATION",
                default_sla_hours=24,
                icon_name="Trash2",
                description="Uncollected municipal waste bins, illegal public trash piles, or missed scheduled collection."
            ),
            ComplaintCategory(
                code="STREETLIGHT_OUT",
                name="Streetlight Malfunction / Dark Zone",
                default_department_code="ELECTRICAL",
                default_sla_hours=36,
                icon_name="LightbulbOff",
                description="Non-functioning public light poles, flickering lamps, or damaged electrical wiring."
            ),
            ComplaintCategory(
                code="WATER_LEAK",
                name="Water Pipeline Leakage / Low Pressure",
                default_department_code="WATER",
                default_sla_hours=24,
                icon_name="Droplets",
                description="Surface water pipe bursts, water main flooding, or contaminated water complaints."
            ),
            ComplaintCategory(
                code="DRAINAGE_BLOCK",
                name="Blocked Storm Drain / Waterlogging",
                default_department_code="ROADS",
                default_sla_hours=24,
                icon_name="Waves",
                description="Clogged storm drains causing street water accumulation during rain events."
            ),
            ComplaintCategory(
                code="TRAFFIC_SIGNAL",
                name="Traffic Signal Grid Failure",
                default_department_code="ELECTRICAL",
                default_sla_hours=12,
                icon_name="TrafficCone",
                description="Intersectional signal lights blacked out or displaying incorrect phasing."
            )
        ]
        cat_map = {}
        for c in categories:
            db.add(c)
            await db.flush()
            cat_map[c.code] = c

        # 4. Seed Municipal Services
        svc_cat = ServiceCategory(
            code="CIVIC_PERMITS",
            name="Civic Permits & Licenses",
            description="Official city certifications, building approvals, and trade permits.",
            icon_name="FileText",
            display_order=1
        )
        db.add(svc_cat)
        await db.flush()

        services = [
            MunicipalService(
                department_id=dept_map["WATER"].id,
                category_id=svc_cat.id,
                code="NEW_WATER_CONNECTION",
                title="Application for New Residential Water Supply Line",
                description="Formal municipal application for laying domestic water connection pipe to newly constructed residential property.",
                eligibility_criteria="Property ownership deed or verified registered lease deed with municipal ward clearance.",
                fee_amount=150.00,
                sla_turnaround_days=10,
                required_documents="Property Deed, Identity Proof, Site Plumbing Blueprint",
                is_online_submission=True
            ),
            MunicipalService(
                department_id=dept_map["ROADS"].id,
                category_id=svc_cat.id,
                code="ROAD_CUTTING_PERMIT",
                title="Utility Road Cutting & Trenching Permission",
                description="Application by contractors or telecom utilities to dig public roadways for cable laying or plumbing.",
                eligibility_criteria="Licensed utility contractor registration certificate and bank guarantee.",
                fee_amount=500.00,
                sla_turnaround_days=7,
                required_documents="Excavation Route Map, Traffic Mitigation Plan, Security Deposit Receipt",
                is_online_submission=True
            )
        ]
        for s in services:
            db.add(s)
        await db.flush()

        # 5. Seed Demo Users
        # Admin User
        admin_user = User(
            email="admin@smartcity360.local",
            hashed_password=get_password_hash("AdminSecurePass2026!"),
            full_name="Administrator Sarah Jenkins",
            phone_number="+1-555-010-0001",
            is_active=True,
            is_verified=True,
            roles=[roles[ROLE_CITY_ADMIN]]
        )
        db.add(admin_user)

        # Citizen User
        citizen_user = User(
            email="citizen@smartcity360.local",
            hashed_password=get_password_hash("CitizenSecurePass2026!"),
            full_name="Marcus Vance (Resident)",
            phone_number="+1-555-010-0042",
            is_active=True,
            is_verified=True,
            roles=[roles[ROLE_CITIZEN]]
        )
        db.add(citizen_user)
        await db.flush()

        cit_profile = CitizenProfile(
            user_id=citizen_user.id,
            address_line="742 Evergreen Terrace, Ward 4",
            ward_number=4,
            zone_name="Central Urban Zone",
            preferred_language="en",
            emergency_contact="+1-555-019-9988"
        )
        db.add(cit_profile)

        # Staff User (Roads Dept)
        staff_user = User(
            email="staff.roads@smartcity360.local",
            hashed_password=get_password_hash("StaffSecurePass2026!"),
            full_name="Engineer Liam O'Connor",
            phone_number="+1-555-010-0205",
            is_active=True,
            is_verified=True,
            roles=[roles[ROLE_DEPT_STAFF], roles[ROLE_FIELD_STAFF]]
        )
        db.add(staff_user)
        await db.flush()

        staff_profile = DepartmentStaff(
            user_id=staff_user.id,
            department_id=dept_map["ROADS"].id,
            employee_badge="ENG-RDS-2044",
            designation="Senior Pavement Maintenance Engineer",
            is_field_responder=True,
            is_available=True
        )
        db.add(staff_profile)
        await db.flush()

        # 6. Seed Sample Complaints (Realistic GPS in Metro Corridor)
        complaints_data = [
            (
                "Severe Asphalt Pothole near Central Metro Station",
                "Deep 15cm pothole in the left carriage lane causing vehicle tire rim damages and significant traffic slowdowns during morning rush hour.",
                "POTHOLE",
                "ROADS",
                "HIGH",
                12.971598,
                77.594562,
                "MG Road Junction, Ward 4",
                4
            ),
            (
                "Commercial Waste Dump Overflowing onto Pedestrian Sidewalk",
                "Four large commercial waste containers overflowing with organic and plastic refuse, blocking wheelchair ramp and emitting foul odor.",
                "GARBAGE",
                "SANITATION",
                "MEDIUM",
                12.975200,
                77.598400,
                "Commercial Street Market Gate 3",
                4
            ),
            (
                "Public Streetlight Cluster Outage on Elm Avenue",
                "Five consecutive LED streetlights unlit along the pedestrian boulevard creating a dark hazard for night commuters.",
                "STREETLIGHT_OUT",
                "ELECTRICAL",
                "LOW",
                12.968400,
                77.589100,
                "Elm Avenue, Sector 7",
                7
            )
        ]

        for idx, (title, desc, cat_code, dept_code, prio, lat, lon, addr, ward) in enumerate(complaints_data, 1):
            comp = Complaint(
                ticket_number=f"CMP-20260912-000{idx}",
                citizen_id=citizen_user.id,
                category_id=cat_map[cat_code].id,
                department_id=dept_map[dept_code].id,
                title=title,
                description=desc,
                priority=prio,
                status="UNDER_REVIEW" if idx == 1 else "NEW",
                latitude=lat,
                longitude=lon,
                location_address=addr,
                ward_number=ward,
                sla_due_at=datetime.now(timezone.utc) + timedelta(hours=48),
                is_escalated=False
            )
            db.add(comp)
            await db.flush()

            db.add(ComplaintStatusHistory(
                complaint_id=comp.id,
                from_status="NONE",
                to_status=comp.status,
                changed_by_user_id=citizen_user.id,
                reason="Lodge via Citizen Portal with location pin."
            ))

        # 7. Seed Emergency Squads & Incidents
        squad = EmergencyResponseTeam(
            unit_identifier="RESCUE-UNIT-04",
            department_id=dept_map["EMERGENCY"].id,
            service_type="FIRE_RESCUE",
            base_station_name="Central District Fire Station #1",
            is_available=True,
            active_crew_count=6,
            current_latitude=12.9720,
            current_longitude=77.5950
        )
        db.add(squad)

        # 8. Seed Public Facilities
        facilities = [
            Facility(
                facility_code="FAC-HOSP-01",
                name="Metropolitan General Hospital & Trauma Center",
                category="HOSPITAL",
                address="100 Hospital Drive, Ward 2",
                latitude=12.9740,
                longitude=77.5920,
                contact_phone="+1-555-019-1111",
                operating_hours="24/7",
                is_operational=True,
                is_wheelchair_accessible=True
            ),
            Facility(
                facility_code="FAC-FIRE-01",
                name="Central Fire & Rescue Station #1",
                category="FIRE_STATION",
                address="45 Civic Center Plaza",
                latitude=12.9725,
                longitude=77.5948,
                contact_phone="+1-555-019-2222",
                operating_hours="24/7",
                is_operational=True,
                is_wheelchair_accessible=True
            ),
            Facility(
                facility_code="FAC-POLICE-01",
                name="Central Police Precinct HQ",
                category="POLICE",
                address="12 Justice Boulevard",
                latitude=12.9710,
                longitude=77.5960,
                contact_phone="+1-555-019-3333",
                operating_hours="24/7",
                is_operational=True,
                is_wheelchair_accessible=True
            )
        ]
        for f in facilities:
            db.add(f)

        # 9. Seed Announcements
        bulletin = Announcement(
            title="Scheduled Water Supply Maintenance in Wards 4 & 5",
            summary="Pressure testing of the 600mm feeder water main will occur between 01:00 and 05:00 tomorrow.",
            content="Residents in Ward 4 and Ward 5 are advised that municipal water pressure may be reduced during nocturnal pipeline calibration.",
            category="WATER_MAINTENANCE",
            priority="NORMAL",
            department_id=dept_map["WATER"].id,
            published_at=datetime.now(timezone.utc),
            expires_at=datetime.now(timezone.utc) + timedelta(days=2),
            is_active=True
        )
        db.add(bulletin)

        await db.commit()
        print("[SUCCESS] Municipal seed dataset loaded successfully.")

if __name__ == "__main__":
    asyncio.run(seed_data())
