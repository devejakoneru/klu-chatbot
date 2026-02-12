import json

DATA_FILE = "knowledge_base/klu_data.json"


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def handle_user_query(query):
    data = load_data()
    q = query.lower()

    # ======================================
    # LMS & ACADEMIC PORTAL (CHECK FIRST)
    # ======================================

    if "lms" in q and "upload" in q:
        return "text", data["portals"]["lms_upload_rules"]

    if "academic portal" in q and "upload" in q:
        return "text", data["portals"]["academic_upload_rules"]

    # ======================================
    # ERP PAYMENT
    # ======================================

    if "erp" in q and ("pay" in q or "payment" in q or "fee" in q):
        return "text", data["erp_payment_procedure"]

    # ======================================
    # HOSTEL RULES
    # ======================================

    if "hostel" in q:
        h = data["hostel_rules"]

        response = (
            f"{h['summary']}\n\n"
            f"First Year Timing: {h['timings_attendance']['first_year']}\n"
            f"Seniors Timing: {h['timings_attendance']['seniors']}\n"
            f"Study Hours: {h['timings_attendance']['study_hours']}\n\n"
            f"Visitors: {h['visitors']}\n"
            f"Prohibited Items: {h['prohibited_items']}\n"
            f"Property & Safety: {h['property_safety']}\n"
            f"Conduct: {h['conduct']}\n"
            f"Meals: {h['meals']}\n"
            f"Loss Liability: {h['loss_liability']}"
        )

        return "text", response

    # ======================================
    # EXAMS
    # ======================================

    if "exam" in q:
        return "text", data["exams"]

    # ======================================
    # SCHOLARSHIPS
    # ======================================

    if "scholarship" in q:
        return "text", data["scholarship"]

    # ======================================
    # LEADERSHIP / HIERARCHY
    # ======================================

    if any(word in q for word in ["chancellor", "chairman", "president", "vice chancellor", "dean"]):
        return "text", data["leadership"]

    # ======================================
    # LIBRARY
    # ======================================

    if "library" in q or "book" in q:
        lib = data["library"]
        return "text", f"{lib['timings']}\n{lib['books']}"

    # ======================================
    # FEES
    # ======================================

    if "fee" in q:
        f = data["fees"]

        response = (
            f"{f['summary']}\n\n"
            f"B.Tech: {f['btech']['hyderabad']}\n\n"
            f"MBA: {f['mba']['guntur']}\n\n"
            f"Other UG: {f['ug_programs']}\n"
            f"PG Programs: {f['pg_programs']}\n\n"
            f"Hostel Fees: {f['hostel']['guntur']}"
        )

        return "text", response

    # ======================================
    # GENERAL RULES (AFTER SPECIFIC CHECKS)
    # ======================================

    if "rules" in q or "college rules" in q:
        r = data["rules"]

        response = (
            f"{r['summary']}\n\n"
            f"Attendance: {r['academic_conduct']['attendance']}\n"
            f"Evaluation: {r['academic_conduct']['evaluation']}\n"
            f"Integrity: {r['academic_conduct']['integrity']}\n\n"
            f"Discipline: {r['code_of_conduct']['discipline']}\n"
            f"Prohibited: {r['code_of_conduct']['prohibited']}\n"
            f"Dress Code: {r['code_of_conduct']['dress_code']}"
        )

        return "text", response

    # ======================================
    # PORTALS
    # ======================================

    if "portal" in q or "website" in q or "link" in q:
        p = data["portals"]

        response = (
            f"Official Website: {p['official_website']}\n"
            f"ERP Portal: {p['erp']}\n"
            f"LMS Portal: {p['lms']}\n"
            f"Academic Portal: {p['academics']}\n"
            f"Admissions Portal: {p['admissions']}"
        )

        return "text", response

    # ======================================
    # IMAGES
    # ======================================

    if "campus map" in q:
        return "image", data["images"]["map"]

    if "campus view" in q or "campus image" in q:
        return "image", data["images"]["campus"]

    if "logo" in q:
        return "image", data["images"]["logo"]

    # ======================================
    # FALLBACK
    # ======================================

    return "text", "I can help with admissions, fees, scholarships, exams, hostel, placements, leadership, library, portals, LMS, academic portal, and campus information."
