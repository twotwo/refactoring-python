from __future__ import annotations  # NameError in use before define

from dataclasses import dataclass
from typing import List


@dataclass
class Person:
    name: str
    photo: Photo


@dataclass
class Photo:
    title: str
    date: str
    location: str


def render_to_html(person: Person):
    def render_person(person):
        result = []
        result.append(f"<p>{person.name}</p>")
        result.append(emit_photo_data(person.photo))
        return "\n".join(result)

    def list_recent_photos(photos: List[Photo]):
        return "\n".join([f"<div>{emit_photo_data(p)}</div>" for p in photos if p.date > resent_date()])

    def emit_photo_data(photo: Photo):
        result = []
        result.append(f"<p>title: {photo.title}</p>")
        result.append(f"<p>date: {photo.date}</p>")
        result.append(f"<p>location: {photo.location}</p>")
        return "\n".join(result)

    def resent_date():
        return "2021-11-27"

    print("=== render_person ===\n", render_person(person))
    print("=== list_recent_photos ===\n", list_recent_photos([person.photo]))


def render_to_html_stage1(person: Person):
    print("=== stage 1(6.1 Extract Function) ===")

    def extract_function(photo: Photo):  # 6.1 Extract Function, a short time function
        return "\n".join([f"<p>title: {photo.title}</p>", f"<p>date: {photo.date}</p>"])

    def render_person(person):  # First caller
        result = []
        result.append(f"<p>{person.name}</p>")
        result.append(extract_function(person.photo))  # 6.2 Inline Function
        result.append(f"<p>location: {person.photo.location}</p>")  # 6.2
        return "\n".join(result)

    def list_recent_photos(photos: List[Photo]):  # Next caller
        return "\n".join(
            [
                f"<div>{extract_function(photo)}<p>location: {photo.location}</p></div>"
                for photo in photos
                if photo.date > resent_date()
            ]
        )

    def emit_photo_data(photo: Photo):  # Third caller
        result = []
        result.append(extract_function(photo))
        result.append(f"<p>location: {photo.location}</p>")
        return "\n".join(result)

    def resent_date():
        return "2021-11-27"

    print("=== render_person ===\n", render_person(person))
    print("=== list_recent_photos ===\n", list_recent_photos([person.photo]))


def render_to_html_stage2(person: Person):
    print("=== stage 2(6.5 Change Function Declaration) ===")

    def emit_photo_data(photo: Photo):  # repalce old emit_photo_data() with extract_function()
        return "\n".join([f"<p>title: {photo.title}</p>", f"<p>date: {photo.date}</p>"])

    def render_person(person):
        result = []
        result.append(f"<p>{person.name}</p>")
        result.append(emit_photo_data(person.photo))
        result.append(f"<p>location: {person.photo.location}</p>")
        return "\n".join(result)

    def list_recent_photos(photos: List[Photo]):
        return "\n".join([f"<div>{emit_photo_data(p)}</div>" for p in photos if p.date > resent_date()])

    def resent_date():
        return "2021-11-27"

    print("=== render_person ===\n", render_person(person))
    print("=== list_recent_photos ===\n", list_recent_photos([person.photo]))


if __name__ == "__main__":
    person = Person(name="lee", photo=Photo("profile", "2021-11-27 19:48:24", "beijing"))
    render_to_html(person)
    # render_to_html_stage1(person)
    render_to_html_stage2(person)
