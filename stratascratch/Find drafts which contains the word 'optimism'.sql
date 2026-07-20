---Find all files from the table whose filename starts with 'draft' and whose contents contain the word 'optimism'. Output all columns.
select *
from google_file_store
where filename like 'draft%'
    and contents like '%optimism%'