export ts_env='dev'
twitch_stitch_root="${PWD%/*}"
echo "\n"
echo "start database migrations"

cd ./database
if [ ! -d ./venv ]; then
    rm -rf ./venv
    rm -rf ./__pycache__
    virtualenv ./venv -p /usr/local/bin/python3
    source venv/bin/activate
    pip3 install --process-dependency-links -r requirements.txt
    cd $twitch_stitch_root/ts_shared
    pip3 install --process-dependency-links -e ./ts_config
    deactivate
fi

source venv/bin/activate
alembic downgrade base && alembic upgrade head

echo "done database migrations"
echo "\n"
