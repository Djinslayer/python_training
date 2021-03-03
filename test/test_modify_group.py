from model.group import Group
from random import randrange

def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='', header="", footer=""))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Group_Mod", header="Test 08.02.21_mod", footer="test 08.02.21_mod")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="modify name"))
#    old_groups = app.group.get_group_list()
#    group = Group(name="modify")
#    group.id = old_groups[0].id
#    app.group.modify_first_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="modify header"))
#    old_groups = app.group.get_group_list()
#    group = Group(header="modify header")
#    group.id = old_groups[0].id
#    app.group.modify_first_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)