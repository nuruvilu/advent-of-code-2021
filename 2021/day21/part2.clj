
(require '[clojure.string :as string])

(defn to-int [string]
  (Integer/parseInt string))

(defn solve [input-list])

(println (solve (string/split-lines (slurp "input.txt"))))
