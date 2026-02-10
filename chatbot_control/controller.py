import json

DATA_FILE = "knowledge_base/klu_data.json"

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def handle_user_query(query):
    data = load_data()
    q = query.lower()

    # ---- HOSTEL RULES (MUST BE EARLY) ----
    if "hostel" in q:
        h = data["hostel_rules"]
        response = (
            "🏠 **KL University Hostel Rules & Regulations**\n\n"
            f"**Timings:**\n"
            f"- First Years: {h['timings_attendance']['first_year']}\n"
            f"- Seniors: {h['timings_attendance']['seniors']}\n"
            f"- Study Hours: {h['timings_attendance']['study_hours']}\n\n"
            f"**Visitors:** {h['visitors']}\n\n"
            f"**Prohibited Items:** {h['prohibited_items']}\n\n"
            f"**Property & Safety:** {h['property_safety']}\n\n"
            f"**Conduct:** {h['conduct']}\n\n"
            f"**Meals:** {h['meals']}\n\n"
            f"**Loss / Liability:** {h['loss_liability']}\n\n"
            "📌 **Administrative Rules**\n"
            f"- Fee Payment: {h['administrative']['fee_payment']}\n"
            f"- Room Allotment: {h['administrative']['room_allotment']}\n"
            f"- Vacating Policy: {h['administrative']['vacating']}"
        )
        return "text", response

    # ---- RULES ----
    if q.strip() == "rules" or "college rules" in q:
        r = data["rules"]
        response = (
            "📘 **KL University Rules Overview**\n\n"
            f"**Attendance:** {r['academic_conduct']['attendance']}\n"
            f"**Evaluation:** {r['academic_conduct']['evaluation']}\n"
            f"**Discipline:** {r['code_of_conduct']['discipline']}\n"
            f"**Dress Code:** {r['code_of_conduct']['dress_code']}\n"
            f"**Prohibited Activities:** {r['code_of_conduct']['prohibited']}"
        )
        return "text", response

    # ---- FEES ----
    if "fee" in q or "fees" in q or "fee structure" in q:
        f = data["fees"]
        response = (
            "💰 **KL University Fee Structure (Approximate)**\n\n"
            f"**B.Tech (Hyderabad Campus):** {f['btech']['hyderabad']}\n\n"
            f"**MBA (Guntur Campus):** {f['mba']['guntur']}\n\n"
            f"**Other UG Programs:** {f['ug_programs']}\n"
            f"**PG Programs:** {f['pg_programs']}\n\n"
            "🏠 **Hostel Fees (Guntur Campus):**\n"
            f"{f['hostel']['guntur']}"
        )
        return "text", response

    # ---- LIBRARY ----
    # ---- LIBRARY ----
    # ---- LIBRARY ----
    if "library" in q or "book" in q:
        lib = data.get("library", {})
        timings = lib.get("timings", "Library timing information not available.")
        books = lib.get("books", "Book borrowing information not available.")
        return "text", f"{timings} {books}"

    # ---- OFFICIAL LINKS / PORTALS ----
    if (
        "official" in q or
        "website" in q or
        "link" in q or
        "portal" in q or
        "erp" in q or
        "lms" in q or
        "academics" in q
    ):
        p = data["portals"]
        response = (
            "🌐 **KL University Official Links**\n\n"
            f"**Official Website:** {p['official_website']}\n"
            f"**ERP Portal:** {p['erp']}\n"
            f"**LMS Portal:** {p['lms']}\n"
            f"**Academics Portal:** {p['academics']}\n"
            f"**Admissions Portal:** {p['admissions']}"
        )
        return "text", response

    # ---- IMAGES ----
    if "logo" in q:
        return "image", data["images"]["logo"]

    if "campus image" in q or "college image" in q:
        return "image", data["images"]["campus"]

    if "map" in q:
        return "image", data["images"]["map"]

    if "route" in q:
        return "image", data["images"]["route"]

    # ---- FALLBACK (MUST BE LAST) ----
    return "text", "You can ask about rules, fees, hostel rules, library, portals, campus images, logo, or route map."
