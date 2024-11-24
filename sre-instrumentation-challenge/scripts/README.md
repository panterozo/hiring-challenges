
# 404 Error Codes

With the following cicle, you can produce 404 in the API solution

Just copy and paste the following command into a terminal

´´´
$ counter=0; while true; do curl --location --request GET "http://localhost:5000/api/buckets/-1"; counter=$((counter+1)); echo "You have called the API $counter times"; done
´´´