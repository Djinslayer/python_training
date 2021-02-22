from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='', header="", footer=""))
    app.group.modify_first_group(Group(name="Group_Mod", header="Test 08.02.21_mod", footer="test 08.02.21_mod"))


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(header="modify name"))
    app.group.modify_first_group(Group(name="modify"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modify header"))
    app.group.modify_first_group(Group(header="modify header"))
