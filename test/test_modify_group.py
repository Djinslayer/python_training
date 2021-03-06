from model.group import Group
from random import randrange


def test_modify_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='', header="", footer=""))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Group_Mod", header="Test 08.02.21_mod", footer="test 08.02.21_mod")
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_some_group(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name='', header="", footer=""))
#    old_groups = app.group.get_group_list()
#    index = randrange(len(old_groups))
#    group = Group(name="Group_Mod", header="Test 08.02.21_mod", footer="test 08.02.21_mod")
#    group.id = old_groups[index].id
#    app.group.modify_group_by_index(index, group)
#    assert len(old_groups) == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups[index] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)