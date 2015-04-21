__author__ = 'Властелин Вселенной'
from model.parameters import Contact
import random


def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="add", lastname="add"))

    group = orm.get_group_list()[0]
    contacts_not_in_group = orm.get_contacts_not_in_group(group)
    contacts_in_group = orm.get_contacts_in_group(group)
    contact = random.choice(contacts_not_in_group)
    app.contact.select_contact_by_id_for_contact_to_group(contact.id)
    app.contact.add_contact_to_group()
    new_contacts_not_in_group = orm.get_contacts_not_in_group(group)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    assert len(contacts_in_group) == len(new_contacts_in_group) - 1
    assert len(contacts_not_in_group) == len(new_contacts_not_in_group) + 1




