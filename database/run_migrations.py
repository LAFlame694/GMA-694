from database.migrations.migration_004_add_job_id_to_invoices import migrate as m1
def run_migrations():
    m1()

if __name__ == "__main__":
    run_migrations()
