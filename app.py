[     UTC     ] Logs for gesner-deslandes-spinning-name-gf7b7hxuvq7dd5kcapp4qbx.streamlit.app/

────────────────────────────────────────────────────────────────────────────────────────

[18:34:48] 🚀 Starting up repository: 'gesner-deslandes-spinning-name', branch: 'main', main module: 'app.py'

[18:34:48] 🐙 Cloning repository...

[18:34:49] 🐙 Cloning into '/mount/src/gesner-deslandes-spinning-name'...

[18:34:49] 🐙 Cloned repository!

[18:34:49] 🐙 Pulling code changes from Github...

[18:34:50] 📦 Processing dependencies...


──────────────────────────────────────── uv ───────────────────────────────────────────


Using uv pip install.

Using Python 3.14.4 environment at /home/adminuser/venv

Resolved 42 packages in 378ms

Prepared 42 packages in 1.32s

Installed 42 packages in 105ms

 + altair==6.1.0

 + anyio==4.13.0

 + attrs==26.1.0

 + blinker==1.9.0

 + cachetools==7.1.0

 + certifi==2026.4.22

 + charset-normalizer==3.4.7

 + click==8.3.3

 + gitdb==4.0.12[2026-05-03 18:34:52.389262] 

 + gitpython==3.1.49

 + h11==0.16.0

 + httptools==0.7.1

 + idna==3.13

 + itsdangerous==2.2.0

 + jinja2==3.1.6[2026-05-03 18:34:52.389444] 

 + jsonschema==4.26.0

 + jsonschema-specifications==2025.9.1

 + markupsafe==3.0.3

 + narwhals==2.20.0

 + numpy==2.4.4

 [2026-05-03 18:34:52.389623] + packaging==26.2

 + pandas==3.0.2

 + pillow==12.2.0

 + protobuf==7.34.1

 + pyarrow==24.0.0

 [2026-05-03 18:34:52.389832] + pydeck==0.9.2

 + python-dateutil==2.9.0.post0

 + python-multipart==0.0.27

 + [2026-05-03 18:34:52.390058] referencing==0.37.0

 + requests==2.33.1

 + rpds-py==0.30.0

 +[2026-05-03 18:34:52.390208]  six==1.17.0

 + smmap==5.0.3

 + starlette==1.0.0

 +[2026-05-03 18:34:52.390314]  streamlit==1.57.0

 + tenacity==9.1.4

 + toml==0.10.2

 + [2026-05-03 18:34:52.390415] typing-extensions==4.15.0

 + urllib3==2.6.3

 + uvicorn==0.46.0

 [2026-05-03 18:34:52.390509] + watchdog==6.0.0

 + websockets==16.0

Checking if Streamlit is installed

Found Streamlit version 1.57.0 in the environment

Installing rich for an improved exception logging

Using uv pip install.

Using Python 3.14.4 environment at /home/adminuser/venv

Resolved 4 packages in 117ms

Prepared 4 packages in 84ms

Installed 4 packages in 9ms

 + [2026-05-03 18:34:53.761548] markdown-it-py==4.0.0

 + mdurl==0.1.2

 + pygments==2.20.0

 + rich==15.0.0


────────────────────────────────────────────────────────────────────────────────────────


[18:34:53] 🐍 Python dependencies were installed from /mount/src/gesner-deslandes-spinning-name/requirements.txt using uv.

Check if streamlit is installed

Streamlit is already installed

[18:34:55] 📦 Processed dependencies!

2026-05-03 18:34:56.335 Uvicorn server started on 0.0.0.0:8501




[18:37:50] 🐙 Pulling code changes from Github...

[18:37:51] 📦 Processing dependencies...

[18:37:51] 📦 Processed dependencies!

[18:37:52] 🔄 Updated app!

[18:40:48] 🐙 Pulling code changes from Github...

[18:40:49] 📦 Processing dependencies...

[18:40:49] 📦 Processed dependencies!

[18:40:50] 🔄 Updated app!

[18:42:29] 🐙 Pulling code changes from Github...

[18:42:30] 📦 Processing dependencies...

[18:42:30] 📦 Processed dependencies!

[18:42:31] 🔄 Updated app!

[18:46:05] 🐙 Pulling code changes from Github...

[18:46:07] 📦 Processing dependencies...

[18:46:07] 📦 Processed dependencies!

[18:46:08] 🔄 Updated app!

[18:48:29] 🐙 Pulling code changes from Github...

[18:48:30] 📦 Processing dependencies...

[18:48:30] 📦 Processed dependencies!

[18:48:32] 🔄 Updated app!

[19:00:57] 🐙 Pulling code changes from Github...

[19:00:58] 📦 Processing dependencies...

[19:00:58] 📦 Processed dependencies!

[19:01:00] 🔄 Updated app!

[19:02:57] 🐙 Pulling code changes from Github...

[19:02:58] 📦 Processing dependencies...

[19:02:58] 📦 Processed dependencies!

[19:02:59] 🔄 Updated app!

2026-05-03 19:30:03.815 Session with id 29ca258f-aa03-4caa-863b-0d79e79b4371 is already connected! Connecting to a new session.

ConnectionClosedError exception in shielded future

future: <Future finished exception=ConnectionClosedError(None, Close(code=<CloseCode.INTERNAL_ERROR: 1011>, reason='keepalive ping timeout'), None)>

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.14/site-packages/websockets/legacy/protocol.py", line 1276, in close_connection

    await self.transfer_data_task

  File "/home/adminuser/venv/lib/python3.14/site-packages/websockets/legacy/protocol.py", line 940, in transfer_data

    message = await self.read_message()

              ^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.14/site-packages/websockets/legacy/protocol.py", line 1010, in read_message

    frame = await self.read_data_frame(max_size=self.max_size)

            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.14/site-packages/websockets/legacy/protocol.py", line 1087, in read_data_frame

    frame = await self.read_frame(max_size)

            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.14/site-packages/websockets/legacy/protocol.py", line 1144, in read_frame

    frame = await Frame.read(

            ^^^^^^^^^^^^^^^^^

    ...<4 lines>...

    )

    ^

  File "/home/adminuser/venv/lib/python3.14/site-packages/websockets/legacy/framing.py", line 70, in read

    data = await reader(2)

           ^^^^^^^^^^^^^^^

  File "/usr/local/lib/python3.14/asyncio/streams.py", line 769, in readexactly

    await self._wait_for_data('readexactly')

  File "/usr/local/lib/python3.14/asyncio/streams.py", line 539, in _wait_for_data

    await self._waiter

asyncio.exceptions.CancelledError


The above exception was the direct cause of the following exception:


websockets.exceptions.ConnectionClosedError: sent 1011 (internal error) keepalive ping timeout; no close frame received

[20:11:21] 🐙 Pulling code changes from Github...

[20:11:22] 📦 Processing dependencies...

[20:11:22] 📦 Processed dependencies!

[20:11:23] 🔄 Updated app!

[20:13:43] 🐙 Pulling code changes from Github...

[20:13:44] 📦 Processing dependencies...

[20:13:44] 📦 Processed dependencies!

[20:13:45] 🔄 Updated app!

main
deslandes1/gesner-deslandes-spinning-name/main/app.py
