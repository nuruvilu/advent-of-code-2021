
(require '[clojure.string :as string])

(def openners {\{ \}, \< \>, \( \), \[ \]})
(def points {\) 3, \] 57, \} 1197, \> 25137})

(defn score [line stack]
  (if (empty? line)
    0
    (if (contains? openners (first line))
      (score (rest line) (cons (first line) stack))
      (if (not= (openners (first stack)) (first line))
        (points (first line))
        (score (rest line) (rest stack))))))

(defn solve [input-list] (reduce + (map #(score % '()) input-list)))

(println (solve (string/split-lines (slurp "input.txt"))))
