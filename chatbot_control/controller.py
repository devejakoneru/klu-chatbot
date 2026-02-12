import json

DATA_FILE = "knowledge_base/klu_data.json"


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def handle_user_query(query):
    data = load_data()
    q = query.lower()

    # ================= LMS & ACADEMIC PORTAL =================
    if "lms" in q and "upload" in q:
        rules = data["digital_portals"]["lms"]["upload_rules"]
        return "text", "\n".join(rules)

    if ("academic portal" in q or "academics" in q) and "upload" in q:
        rules = data["digital_portals"]["academic_portal"]["upload_rules"]
        return "text", "\n".join(rules)

    # ================= ERP PAYMENT =================
    if "erp" in q and ("pay" in q or "payment" in q or "fee" in q):
        return "text", "\n".join(data["fees"]["payment_procedure"])

    # ================= HOSTEL =================
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
            f"Loss Liability: {h['loss_liability']}\n\n"
            f"Hostel Fee Payment: {h['administrative_rules']['fee_payment']}\n"
            f"Room Allotment: {h['administrative_rules']['room_allotment']}\n"
            f"Vacating: {h['administrative_rules']['vacating']}"
        )

        return "text", response

    # ================= EXAMS =================
    if "exam" in q:
        return "text", data["exams"]

    # ================= SCHOLARSHIPS =================
    if "scholarship" in q:
        s = data["scholarships"]
        return "text", "\n".join(s.values())

    # ================= LEADERSHIP =================
    if any(word in q for word in ["chancellor", "president", "vice chancellor", "dean"]):
        a = data["administration"]
        return "text", (
            f"Chancellor: {a['chancellor_president']}\n"
            f"Vice Presidents: {', '.join(a['vice_presidents'])}\n"
            f"Vice Chancellor: {a['vice_chancellor']}\n"
            f"Registrar: {a['registrar']}"
        )

    # ================= LIBRARY =================
    if "library" in q or "book" in q:
        lib = data["library"]
        return "text", f"{lib['timings']}\n{lib['books']}"

    # ================= FEES =================
    if "fee" in q:
        f = data["fees"]
        return "text", (
            f"{f['summary']}\n\n"
            f"B.Tech: {f['btech']}\n\n"
            f"MBA: {f['mba']}\n\n"
            f"Other UG: {f['other_ug']}\n"
            f"PG Programs: {f['pg_programs']}\n\n"
            f"Hostel Fees: {f['hostel_fees']}"
        )

    # ================= RULES =================
    if "rules" in q:
        r = data["rules"]
        return "text", (
            f"{r['summary']}\n\n"
            f"Attendance: {r['academic_conduct']['attendance']}\n"
            f"Evaluation: {r['academic_conduct']['evaluation']}\n"
            f"Integrity: {r['academic_conduct']['integrity']}\n\n"
            f"Discipline: {r['code_of_conduct']['discipline']}\n"
            f"Prohibited: {r['code_of_conduct']['prohibited']}\n"
            f"Dress Code: {r['code_of_conduct']['dress_code']}"
        )

    # ================= PORTALS =================
    if "portal" in q or "website" in q or "link" in q:
        p = data["portals"]
        return "text", (
            f"Official Website: {p['official_website']}\n"
            f"ERP: {p['erp']}\n"
            f"LMS: {p['lms']}\n"
            f"Academic Portal: {p['academics']}\n"
            f"Admissions: {p['admissions']}"
        )

    # ================= IMAGES =================
    if "campus map" in q:
        return "image", data["images"]["map"]

    if "campus" in q:
        return "image", data["images"]["campus"]

    if "logo" in q:
        return "image", data["images"]["logo"]

    # ================= ATTENDANCE =================
    if "attendance" in q:
        return "text", data["attendance_info"]

    # ================= ADMISSIONS =================
    if "admission" in q:
        return "text", "\n".join(data["admissions"]["process"])

    # ================= ADMIN =================
    # ======================================
    # LEADERSHIP / ADMINISTRATION
    # ======================================

    if any(word in q for word in ["chancellor", "president", "vice chancellor", "dean", "registrar", "administration"]):
        a = data["administration"]

        response = (
            f"Chancellor / President: {a['chancellor_president']}\n"
            f"Vice-Presidents: {', '.join(a['vice_presidents'])}\n"
            f"Pro-Chancellor: {a['pro_chancellor']}\n"
            f"Vice-Chancellor: {a['vice_chancellor']}\n"
            f"Pro Vice-Chancellors: {', '.join(a['pro_vice_chancellors'])}\n"
            f"Registrar: {a['registrar']}\n\n"
            "Key Deans:\n"
        )

        for role, name in a["deans"].items():
            response += f"{role}: {name}\n"

        return "text", response

    # ================= FALLBACK =================
    return "text", "I can help with admissions, fees, exams, scholarships, hostel, library, ERP, LMS, and campus info."
