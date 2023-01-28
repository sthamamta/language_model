
python3 count_bigrams.py input/Shakespeare.txt outputs

python3 prob_sentence.py << EOF
n
All the world's a stage.
EOF
echo "With laplace smoothing"
python3 prob_sentence.py << EOF
y
All the world's a stage.
EOF
echo '\n'

echo '\n'
python3 prob_sentence.py << EOF
n
to be or not to be.
EOF
echo "With laplace smoothing"
python3 prob_sentence.py << EOF
y
to be or not to be.
EOF

echo '\n'
python3 prob_sentence.py << EOF
n
astronaut Internet telephone.
EOF
echo "With laplace smoothing"
python3 prob_sentence.py << EOF
y
astronaut Internet telephone.
EOF

echo '\n'
python3 generate_sentence.py<< EOF
n
love
EOF
python3 generate_sentence.py<< EOF
n
sleep
EOF
python3 generate_sentence.py<< EOF
n
twitter
EOF

echo 'using laplace smoothing'
python3 generate_sentence.py<< EOF
y
love
EOF
python3 generate_sentence.py<< EOF
y
sleep
EOF
python3 generate_sentence.py<< EOF
y
twitter
EOF