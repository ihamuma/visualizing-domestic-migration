from api.stat_fi_main import verify_and_create_files

# To initialise the project, run this program to verify the existence of the migration.parquet and employment.parquet files.
# If no files are found, the program automatically creates API requests to create the files. This may take a few moments.

verify_and_create_files()
