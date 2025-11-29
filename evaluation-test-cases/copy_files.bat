@echo off
set SOURCE=.
set DEST=..\evaluation-test-cases

mkdir %DEST% 2>nul

copy %SOURCE%\answer.json %DEST%\
copy %SOURCE%\cache_answer.txt %DEST%\
copy %SOURCE%\cache_submit.json %DEST%\
copy %SOURCE%\gh_counter.py %DEST%\
copy %SOURCE%\logs.jsonl %DEST%\
copy %SOURCE%\logs.py %DEST%\
copy %SOURCE%\order.py %DEST%\
copy %SOURCE%\orders.csv %DEST%\
copy %SOURCE%\shards.json %DEST%\
copy %SOURCE%\shards_optimizer.py %DEST%\
copy %SOURCE%\shards_submit.json %DEST%\
copy %SOURCE%\tree.json %DEST%\

echo Files copied successfully!