query = """

select *
                            from sqlite_master 
                            where type='table' and
                            name = '{table_name}'
                            order by name;
"""