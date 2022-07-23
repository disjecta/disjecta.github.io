import os

static_dir = "public_collect_static"
distill_dir = "public"
 
try:
    os.mkdir(static_dir)
    print(f"Directory '{static_dir}' created successfully")
except FileExistsError:
    print(f"Directory '{static_dir}' already exists")

try:
    os.mkdir(distill_dir)
    print(f"Directory '{distill_dir}' created successfully")
except FileExistsError:
    print(f"Directory '{distill_dir}' already exists")

os.system('pip install -r aaa/deps/pip/prod.pip')

os.system('python3 manage.py collectstatic --noinput \
    --settings aaa.settings.prod \
    --ignore admin \
    --ignore django_non_dark_admin')

os.system('python3 manage.py distill-local --force \
    --settings aaa.settings.prod')
