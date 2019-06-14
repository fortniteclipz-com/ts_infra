export TS_ENV=${1:-'dev'}
twitch_stitch_root="${PWD%/*}"

echo "migrate | start | ts-$TS_ENV"
cd $twitch_stitch_root/ts_infra/migrations
if [ ! -d ./venv ]; then
    echo "migrate | bootstrapping | ts-$TS_ENV"
    rm -rf ./venv
    rm -rf ./__pycache__
    /usr/local/Cellar/python/3.6.5_1/bin/python3 -m venv ./venv
    source venv/bin/activate
    pip3 install --process-dependency-links -r requirements.txt
    pip3 install --process-dependency-links -e $twitch_stitch_root/ts_shared/ts_config
    deactivate
fi

echo "migrate | migrating | ts-$TS_ENV"
source venv/bin/activate
alembic upgrade head
