import json

DATA_FILE = "knowledge_base/klu_data.json"


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def handle_user_query(query):
    data = load_data()
    q = query.lower()

    # ================= RULES =================
    if "rule" in q or "academic conduct" in q or "code of conduct" in q:
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

    # ================= FEES =================
    if "fee" in q or "payment" in q:
        f = data["fees"]
        response = (
            f"{f['summary']}\n\n"
            f"B.Tech: {f['btech']}\n"
            f"MBA: {f['mba']}\n"
            f"Other UG: {f['other_ug']}\n"
            f"PG Programs: {f['pg_programs']}\n"
            f"Hostel Fees: {f['hostel_fees']}\n\n"
            "Payment Procedure:\n"
        )
        for step in f["payment_procedure"]:
            response += f"- {step}\n"
        return "text", response

    # ================= EXAMS =================
    if "exam" in q or "internal" in q or "external" in q:
        e = data["examinations"]
        return "text", (
            f"Exam Pattern:\n\n"
            f"{e['internal_weightage']}\n"
            f"{e['external_weightage']}"
        )

    # ================= SCHOLARSHIPS =================
    if "scholarship" in q:
        s = data["scholarships"]
        return "text", (
            f"Scholarships:\n\n"
            f"Merit: {s['merit_based']}\n"
            f"Marks Based: {s['marks_based']}\n"
            f"Sports: {s['sports']}\n"
            f"Need Based: {s['need_based']}"
        )

    # ================= ADMISSIONS =================
    if "admission" in q or "klcet" in q:
        a = data["admissions"]
        response = "Admission Process:\n\n"
        for step in a["process"]:
            response += f"- {step}\n"
        return "text", response

    # ================= HOSTEL =================
    if "hostel" in q:
        return "text", "Hostel facilities are available with discipline and safety regulations."

    # ================= PLACEMENTS =================
    if "placement" in q or "job" in q or "recruitment" in q:
        p = data["placements"]
        response = "Placement Process:\n\n"
        for step in p["placement_process"]:
            response += f"- {step}\n"
        return "text", response

    # ================= SAFETY =================
    if "safety" in q or "security" in q:
        s = data["campus_safety"]
        return "text", (
            f"Campus Safety:\n"
            f"{s['security']}\n"
            f"{s['cctv']}\n"
            f"{s['anti_ragging']}"
        )

    # ================= LEADERSHIP =================
    if "vice chancellor" in q:
        return "text", f"Vice Chancellor: {data['administration']['vice_chancellor']}"

    if "chancellor" in q:
        return "text", f"Chancellor: {data['administration']['chancellor_president']}"

    if "dean" in q:
        deans = data["administration"]["deans"]
        response = "University Deans:\n\n"
        for role, name in deans.items():
            response += f"{role}: {name}\n"
        return "text", response

    # ================= LIBRARY =================
    if "library" in q or "book" in q:
        l = data["library"]
        return "text", f"{l['timings']}\n{l['books']}"

    # ================= PORTALS =================
    if "erp" in q or "portal" in q:
        p = data["portals"]
        return "text", (
            f"Official Website: {p['official_website']}\n"
            f"ERP: {p['erp']}\n"
            f"LMS: {p['lms']}\n"
            f"Academics: {p['academics']}\n"
            f"Admissions: {p['admissions']}"
        )

    # ================= IMAGES =================
    if "logo" in q:
        return "image", data["images"]["logo"]

    if "campus image" in q:
        return "image", data["images"]["campus"]

    if "map" in q:
        return "image", data["images"]["map"]

    if "route" in q:
        return "image", data["images"]["route"]

    return "text", "I can help with admissions, fees, scholarships, exams, hostel, placements, leadership, library, portals, and campus information."
