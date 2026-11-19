# CampusNotes Tag Search Utility - Navya Sharma (2581354)

def filter_notes_by_tag(notes_list, search_tag):
    if not search_tag:
        return notes_list
    target = search_tag.strip().lower()
    return [note for note in notes_list if note.get('tag') and str(note.get('tag')).strip().lower() == target]
