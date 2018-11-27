export ts_env=${1:-'dev'}
twitch_stitch_root="${PWD%/*}"
migrations_dir=$PWD/migrations

echo "ts_env: $ts_env"
echo "\n"
echo "start migrations"

cd $migrations_dir
if [ ! -d ./venv ]; then
    rm -rf ./venv
    rm -rf ./__pycache__
    virtualenv ./venv -p /usr/local/bin/python3
    source venv/bin/activate
    pip3 install --process-dependency-links -r requirements.txt
    cd $twitch_stitch_root/ts_shared
    pip3 install --process-dependency-links -e ./ts_config
    deactivate
    cd $migrations_dir
fi

source venv/bin/activate
alembic upgrade head

echo "done migrations"
echo "\n"
