export TS_ENV=${1:-'dev'}
twitch_stitch_root="${PWD%/*}"
migrations_dir=$PWD/migrations

echo "TS_ENV: $TS_ENV"
echo "\n"
echo "start migrations"

cd $migrations_dir
if [ ! -d ./venv ]; then
    rm -rf ./venv
    rm -rf ./__pycache__
    /usr/local/Cellar/python/3.6.5_1/bin/python3 -m venv ./venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    cd $twitch_stitch_root/ts_shared
    pip3 install -e ./ts_config
    deactivate
    cd $migrations_dir
fi

source venv/bin/activate
alembic upgrade head

echo "done migrations"
echo "\n"
