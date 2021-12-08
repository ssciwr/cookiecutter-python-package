from . import check_bake, inside_bake


def test_project_tree(cookies):
    bake = cookies.bake(extra_context={'project_slug': 'test_project'})
    check_bake(bake)
