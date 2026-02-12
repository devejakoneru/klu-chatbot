import json
from gan_model.gan import GANResponseEngine
from gan_model.ai_engine import generate_academic_response

DATA_FILE = "knowledge_base/klu_data.json"

gan_engine = GANResponseEngine()


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def enhance_with_gan(text: str) -> str:
    try:
        return gan_engine.generate_response(text)
    except Exception:
        return text


def is_academic_query(query: str) -> bool:
    allowed_keywords = [
        "klu", "university", "fee", "attendance",
        "exam", "hostel", "erp", "placement",
        "cgpa", "study", "subject", "course",
        "syllabus", "academics", "admission",
        "how", "who", "what", "explain"
    ]
    return any(word in query.lower() for word in allowed_keywords)


def handle_user_query(query):
    data = load_data()
    q = query.lower().strip()

    # ==================================================
    # 1️⃣ EXACT MATCH SECTION (Priority JSON)
    # ==================================================

    if q == "rules":
        r = data["rules"]
        response = (
            "📘 **KL University Rules Overview**\n\n"
            f"Attendance: {r['academic_conduct']['attendance']}\n"
            f"Evaluation: {r['academic_conduct']['evaluation']}\n"
            f"Discipline: {r['code_of_conduct']['discipline']}\n"
            f"Dress Code: {r['code_of_conduct']['dress_code']}\n"
            f"Prohibited: {r['code_of_conduct']['prohibited']}"
        )
        return "text", enhance_with_gan(response)

    if q == "fees":
        f = data["fees"]
        response = (
            "💰 **KL University Fee Structure (Approximate)**\n\n"
            f"B.Tech: {f['btech']['hyderabad']}\n"
            f"MBA: {f['mba']['guntur']}\n"
            f"UG Programs: {f['ug_programs']}\n"
            f"PG Programs: {f['pg_programs']}\n"
            f"Hostel Fees: {f['hostel']['guntur']}"
        )
        return "text", enhance_with_gan(response)

    if q == "library":
        lib = data.get("library", {})
        timings = lib.get("timings", "Library timing not available.")
        books = lib.get("books", "Borrowing information not available.")
        return "text", enhance_with_gan(f"{timings}\n{books}")

    if q == "hostel rules":
        h = data["hostel_rules"]
        response = (
            f"Timings:\n"
            f"- First Years: {h['timings_attendance']['first_year']}\n"
            f"- Seniors: {h['timings_attendance']['seniors']}\n"
            f"- Study Hours: {h['timings_attendance']['study_hours']}"
        )
        return "text", enhance_with_gan(response)

    # ==================================================
    # 2️⃣ IMAGE SECTION
    # ==================================================

    if "logo" in q:
        return "image", data["images"]["logo"]

    if "campus image" in q or "college image" in q:
        return "image", data["images"]["campus"]

    if "map" in q:
        return "image", data["images"]["map"]

    if "route" in q:
        return "image", data["images"]["route"]

    # ==================================================
    # 3️⃣ AI SECTION (Complex Queries Only)
    # ==================================================

    # If query has more than 3 words → treat as detailed question
    if len(q.split()) > 3 and is_academic_query(query):
        ai_response = generate_academic_response(query)
        return "text", ai_response

    # ==================================================
    # 4️⃣ FALLBACK
    # ==================================================

    fallback = "You can ask about rules, fees, hostel rules, library, portals, campus images, logo, or route map."
    return "text", enhance_with_gan(fallback)
