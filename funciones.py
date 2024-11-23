# Devuelve true si la canción es válida (pasa los filtros)
def filtros(recording):
    title = recording["title"].lower()
    length = recording.get("length", 0)
    disambiguation = recording.get("disambiguation", "").lower()

    # Filtro por duración
    if length and length < 30000:
        return False

    # Filtro por tipo en el campo "disambiguation"
    if any(keyword in disambiguation for keyword in ["instrumental", "live", "karaoke", "demo", "edit", "video"]):
        return False
    
    # Filtro por versiones alternas en "disambiguation"
    if any(keyword in disambiguation for keyword in ["remix", "acoustic", "rehearsal", "session", "version", "video"]):
        return False
    
    # Filtro para grabaciones sin título
    if not title.strip():
        return False

    # Filtro por tipo en el campo "title"
    if any(keyword in title for keyword in ["(instrumental)", "(live)", "(karaoke)", "(demo)", "(edit)", "(video)"]):
        return False

    # Filtro por palabras adicionales en el título que puedan identificar versiones no estándar
    if any(keyword in title for keyword in ["remix", "acoustic", "rehearsal", "session", "version", "video"]):
        return False

    # Filtro por longitud excesiva del título (indicativo de datos erróneos)
    if len(title) > 100:
        return False

    return True
