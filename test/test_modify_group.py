from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='', header="", footer=""))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="Group_Mod", header="Test 08.02.21_mod", footer="test 08.02.21_mod"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(header="modify name"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="modify"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modify header"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="modify header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)