from setuptools import setup

setup(
    name="electrum-reecoin-server",
    version="0.9",
    scripts=['run_electrum_reecoin_server','electrum-reecoin-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumserver':'src'
        },
    py_modules=[
        'electrumserver.__init__',
        'electrumserver.utils',
        'electrumserver.storage',
        'electrumserver.deserialize',
        'electrumserver.networks',
        'electrumserver.blockchain_processor',
        'electrumserver.server_processor',
        'electrumserver.processor',
        'electrumserver.version',
        'electrumserver.ircthread',
        'electrumserver.stratum_tcp',
        'electrumserver.stratum_http'
    ],
    description="Reecoin Electrum Server",
    author="Thomas Voegtlin, ELM4ever, Propulsion, Sunerok",
    author_email="thomasv1@gmx.de, Propulsion@ReecoinTalk.org, mobilenetzllc@gmail.com",
    license="GNU Affero GPLv3",
    url="https://github.com/spesmilo/electrum-server/, https://github.com/mazaclub/electrum-reecoin-server/",
    long_description="""Server for the Electrum Lightweight Reecoin Wallet"""
)


