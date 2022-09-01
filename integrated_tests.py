""" DataAccessLayer to setup temporary fake dbs to test input/output unit tests and integration testing."""
from pathlib import Path

import pandas as pd
from dateutil.parser import ParserError
from pg_temp import TempDB
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Date,
    Float,
    MetaData,
    String,
    Table,
    VARCHAR,
    Integer,
)
from sqlalchemy.engine import create_engine, url
from sqlalchemy.sql import Delete
from sqlalchemy.sql.sqltypes import DateTime


class DataAccessLayer:
    metadata = MetaData()

    EXAMPLE_TABLE = Table(
        "EXAMPLE_TABLE",
        metadata,
        Column(),
        schema="",
    )

    def db_init(self, db: str) -> None:
        """Create db, and all tables, according to metadata."""
        self.temp_db = TempDB(databases=[db])
        self.conn_string = url.URL.create(
            drivername="postgresql", host=self.temp_db.pg_socket_dir, database=db
        )
        self.engine = create_engine(self.conn_string)
        self.connection = self.engine.connect()
        self.connection.execute("CREATE SCHEMA bp")
        self.metadata.create_all(self.engine)

    def db_destroy(self) -> None:
        """Destroy db, and close connection."""
        self.connection.close()
        self.engine.dispose()
        self.temp_db.cleanup()
        self.tmp_db = None
        self.connection = None
        self.engine = None
        self.conn_string = None

    def db_populate(self, current_test: str) -> None:
        """Populate all tables in temporary db with CSV's."""
        # E.g. current_test = "test_run"
        # CSV's found in ./data/run/tables
        path = current_test.split("_")[1]
        data_dir = Path(__file__).parent.joinpath("data", path, "tables")
        for file in data_dir.iterdir():
            table = getattr(self, file.stem)
            data = pd.read_csv(file.open())
            for col in data.columns:
                # Convert date columns to datetime
                if "date" in col.lower() and not all(
                    data[col].astype("str").str.isnumeric()
                ):
                    try:
                        data[col] = pd.to_datetime(data[col])
                    except ParserError:
                        pass
            for row in data.to_dict(orient="records"):
                self.connection.execute(table.insert().values(row))

    def db_clean(self, current_test: str) -> None:
        """Delete all tables in temporary db."""
        path = current_test.split("_")[1]
        data_dir = Path(__file__).parent.joinpath("data", path, "tables")
        for file in data_dir.iterdir():
            table = getattr(self, file.stem)
            self.connection.execute(Delete(table))
            
class TestInput(TestCase):
    dal = DataAccessLayer()

    @classmethod
    def setUpClass(cls):
        cls.dal.db_init("test")

    @classmethod
    def tearDownClass(cls):
        cls.dal.db_destroy()

    def tearDown(self):
        self.dal.db_clean("test_simple")

    def setUp(self):
        self.dal.db_populate("test_simple")

        
@click.command()
@click.option(
    "-c",
    "--config_file",
    required=True,
    type=click.File(),
    help="File path to configuration.",
)
def main():
    ENGINE = create_db_engine(config["credentials"])
    with ENGINE.begin() as conn:
        ...

# Add parent directory to python path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import run

@patch(".io.get_model_parameters")
@patch(".io.get_data")
@patch(".io.create_db_engine")
def test_run_no_valid_data(self, create_engine, get_data, get_model_parameters):
    """ Test results are not generated when all markets have insufficient non-zero data. """
    create_engine.return_value = self.dal.engine
    
    runner = CliRunner()
    runner.invoke(
        run.main,
        ['-vvv', '-c', '--file', './tests/test_config.json'],
        catch_exceptions=False
    )
    with self.dal.engine.begin() as conn:
        results = .io.get_results(conn)
        
  from unittest import TestCase
from unittest.mock import patch, MagicMock

from click.testing import CliRunner

def save_parameters(_, params, **kwargs):
    nonlocal learned_model_parameters

    #LOGGER.warning("The following Model Parameters were attempted to be saved:\n %s", params)
    learned_model_parameters = params
    store_parameters.side_effect = save_parameters
    
create_db_engine.begin.return_value.__enter__.return_value = None
