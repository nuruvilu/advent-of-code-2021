
(require '[clojure.string :as string])

(defn occurrences [num coll]
  (count (filter #(= num %) coll)))

(defn grow-fish [days-left fish]
  (if (= days-left 0)
    (reduce + fish)
    (grow-fish (dec days-left)
               (conj (vec (map + (rest fish) [0 0 0 0 0 0 (first fish) 0]))
                     (first fish)))))

(defn solve [input]
  (let [starting-fish (map #(Integer/parseInt %) input)
        fish (map #(occurrences % starting-fish) (range 9))]
    {:silver (grow-fish 80 fish), :gold (grow-fish 256 fish)}))

(println (solve (string/split (slurp "input.txt") #",")))
