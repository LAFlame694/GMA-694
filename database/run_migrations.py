from database.migrations.migration_005_add_active_to_parts import migrate as m1
def run_migrations():
    m1()

if __name__ == "__main__":
    run_migrations()
