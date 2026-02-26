from gan_model.gan_engine import GANResponseEnhancer
gan_enhancer = GANResponseEnhancer()

import json

DATA_FILE = "knowledge_base/klu_data.json"


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def handle_user_query(query):
    data = load_data()
    q = query.lower()
    response = None
    msg_type = "text"

    # ================= LMS & ACADEMIC PORTAL =================
    if "lms" in q and "upload" in q:
        response = "\n".join(data["digital_portals"]["lms"]["upload_rules"])

    elif ("academic portal" in q or "academics" in q) and "upload" in q:
        response = "\n".join(data["digital_portals"]["academic_portal"]["upload_rules"])

    # ================= ERP PAYMENT =================
    elif "erp" in q and ("pay" in q or "payment" in q or "fee" in q):
        response = "\n".join(data["fees"]["payment_procedure"])

    # ================= HOSTEL FOOD =================
    elif "food" in q or "mess" in q or "dining" in q:
        m = data["hostel_rules"]["mess"]
        response = f"Breakfast: {m['breakfast']}\nLunch: {m['lunch']}\nDinner: {m['dinner']}"

    # ================= HOSTEL =================
    elif "hostel" in q:
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

    # ================= EXAMS =================
    elif "exam" in q:
        response = data["exams"]

    # ================= SCHOLARSHIPS =================
    elif "scholarship" in q:
        response = "\n".join(data["scholarships"].values())

    # ================= FEES =================
    elif "fee" in q:
        f = data["fees"]
        response = (
            f"{f['summary']}\n\n"
            f"B.Tech: {f['btech']}\n\n"
            f"MBA: {f['mba']}\n\n"
            f"Other UG: {f['other_ug']}\n"
            f"PG Programs: {f['pg_programs']}\n\n"
            f"Hostel Fees: {f['hostel_fees']}"
        )

    # ================= RULES =================
    elif "rules" in q:
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

    # ================= PORTALS =================
    elif "portal" in q or "website" in q or "link" in q:
        p = data["portals"]
        response = (
            f"Official Website: {p['official_website']}\n"
            f"ERP: {p['erp']}\n"
            f"LMS: {p['lms']}\n"
            f"Academic Portal: {p['academics']}\n"
            f"Admissions: {p['admissions']}"
        )

    # ================= IMAGES =================
    elif "campus map" in q:
        return "image", data["images"]["map"]

    elif "campus" in q:
        return "image", data["images"]["campus"]

    elif "logo" in q:
        return "image", data["images"]["logo"]

    # ================= ATTENDANCE =================
    elif "attendance" in q:
        response = data["attendance_info"]

    # ================= ADMISSIONS =================
    elif "admission" in q:
        response = "\n".join(data["admissions"]["process"])

    # ================= PLACEMENTS =================
    elif "placement" in q or "job" in q:
        response = "\n".join(data["placements"]["placement_process"])

    # ================= LEADERSHIP =================
    elif any(word in q for word in ["chancellor", "president", "vice chancellor", "dean", "registrar", "administration", "leadership"]):
        a = data["administration"]
        response = (
            f"Chancellor / President: {a['chancellor_president']}\n"
            f"Vice-Presidents: {', '.join(a['vice_presidents'])}\n"
            f"Pro-Chancellor: {a['pro_chancellor']}\n"
            f"Vice-Chancellor: {a['vice_chancellor']}\n"
            f"Pro Vice-Chancellors: {', '.join(a['pro_vice_chancellors'])}\n"
            f"Registrar: {a['registrar']}\n"
        )

    # ================= FALLBACK =================
    else:
        response = "I can help with admissions, fees, exams, scholarships, hostel, library, ERP, LMS, and campus info."

    if msg_type == "text":
        response = gan_enhancer.enhance(response)

    return msg_type, response