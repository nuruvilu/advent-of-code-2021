
(require '[clojure.string :as string])

(def openners {\{ \}, \< \>, \( \), \[ \]})
(def points {\) 1, \] 2, \} 3, \> 4})

(defn auto-score [stack current-score]
  (if (empty? stack)
    current-score
    (auto-score (rest stack) (+ (* current-score 5)
                                (points (openners (first stack)))))))

(defn score [line stack]
  (if (empty? line)
    (auto-score stack 0)
    (if (contains? openners (first line))
      (score (rest line) (cons (first line) stack))
      (if (not= (openners (first stack)) (first line))
        :corrupted
        (score (rest line) (rest stack))))))

(defn median [nums]
  (let [len (count nums) mid (/ (dec len) 2)]
    (if (= 1 (mod len 2))
      (nth nums mid)
      (/ (+ (nth nums mid) (nth nums (inc mid))) 2))))

(defn solve [input-list]
  (->> (map #(score % '()) input-list)
       (filter #(not= % :corrupted))
       (sort)
       (median)))

(println (solve (string/split-lines (slurp "input.txt"))))
