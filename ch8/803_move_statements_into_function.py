from __future__ import annotations  # NameError in use before define
from dataclasses import dataclass


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
        result.append(f"<p>title: {person.photo.title}</p>")
        result.append(emit_photo_data(person.photo))
        return "\n".join(result)

    def photo_div(p):
        result = [
            "<div>",
            f"<p>title:  {p.title}</p>",
            emit_photo_data(p),
            "</div>",
        ]
        return "\n".join(result)

    def emit_photo_data(photo: Photo):
        result = []
        result.append(f"<p>location: {photo.location}</p>")
        result.append(f"<p>date: {photo.date}</p>")
        return "\n".join(result)

    print("=== render_person ===\n", render_person(person))
    print("=== photo_div ===\n", photo_div(person.photo))


def render_to_html_stage1(person: Person):
    print("=== stage 1(6.1 Extract Function) ===")

    def render_person(person):
        result = []
        result.append(f"<p>{person.name}</p>")
        result.append(ec_new_function(person.photo))
        return "\n".join(result)

    def photo_div(p):
        result = [
            "<div>",
            ec_new_function(p),
            "</div>",
        ]
        return "\n".join(result)

    def emit_photo_data(photo: Photo):
        result = []
        result.append(f"<p>location: {photo.location}</p>")
        result.append(f"<p>date: {photo.date}</p>")
        return "\n".join(result)

    def ec_new_function(photo: Photo):
        return "\n".join([f"<p>{person.name}</p>", f"<p>location: {photo.location}</p>", f"<p>date: {photo.date}</p>"])

    print("=== render_person ===\n", render_person(person))
    print("=== photo_div ===\n", photo_div(person.photo))


def render_to_html_stage2(person: Person):
    print("=== stage 2(6.5 Change Function Declaration) ===")

    def render_person(person):
        result = []
        result.append(f"<p>{person.name}</p>")
        result.append(emit_photo_data(person.photo))
        return "\n".join(result)

    def photo_div(photo: Photo):
        result = [
            "<div>",
            emit_photo_data(photo),
            "</div>",
        ]
        return "\n".join(result)

    def emit_photo_data(photo: Photo):
        return "\n".join([f"<p>{person.name}</p>", f"<p>location: {photo.location}</p>", f"<p>date: {photo.date}</p>"])

    print("=== render_person ===\n", render_person(person))
    print("=== photo_div ===\n", photo_div(person.photo))


if __name__ == "__main__":
    person = Person(name="lee", photo=Photo("profile", "2021-11-27 19:48:24", "beijing"))
    render_to_html(person)
    # render_to_html_stage1(person)
    render_to_html_stage2(person)
