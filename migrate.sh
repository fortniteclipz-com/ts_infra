ts_env=${1:-'dev'}
echo "migrate | start | ts_env=$ts_env"

twitch_stitch_root=${PWD%/*}
cd $twitch_stitch_root/ts_infra/migrations
if [ ! -d ./venv ]; then
    echo "migrate | bootstrapping | ts_env=$ts_env"
    rm -rf ./venv
    rm -rf ./__pycache__
    /usr/local/Cellar/python/3.6.5_1/bin/python3 -m venv ./venv
    source venv/bin/activate
    pip3 install --process-dependency-links -r requirements.txt
    pip3 install --process-dependency-links -e $twitch_stitch_root/ts_shared/ts_config
    deactivate
fi

echo "migrate | migrating | ts_env=$ts_env"
source venv/bin/activate
export TS_ENV=$ts_env
alembic upgrade head

echo "migrate | done | ts_env=$ts_env"
