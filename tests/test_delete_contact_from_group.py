__author__ = 'Властелин Вселенной'
from model.parameters import Contact, Group
import random


def test_delete_contact_from_group(app, orm):
    group_name = "test_group"
    group = Group(name=group_name)
    if len(orm.find_group_in_list_by_name(group))== 0:
        app.group.create_new_group(group)
    if len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create_new_contact_short(Contact(firstname="add", middlename="add", lastname="add"))
    if len(orm.get_contacts_in_group(group)) == 0:
        app.contact.open_contact_page()
        contacts_not_in_group = orm.get_contacts_not_in_group(group)
        contact = random.choice(contacts_not_in_group)
        app.contact.select_contact_by_id_for_contact_to_group(contact.id)
        app.contact.select_group_bottom_dropdown(group_name)
        app.contact.click_add_contact_to_group()
        app.contact.open_contact_page()

    contacts_not_in_group = orm.get_contacts_not_in_group(group)
    contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.select_group_top_dropdown(group_name)
    app.contact.select_contact_by_index(0)
    app.contact.click_remove_contact_from_group()
    new_contacts_not_in_group = orm.get_contacts_not_in_group(group)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    assert len(contacts_in_group) == len(new_contacts_in_group) + 1
    assert len(contacts_not_in_group) == len(new_contacts_not_in_group) - 1
