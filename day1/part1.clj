
(require '[clojure.string :as string])

(defn to-int [string]
  (Integer/parseInt string))

(defn solve [input-list]
  (let [inputs (map to-int input-list)]
    (->> (map vector inputs (rest inputs))
         (map (fn [p] (if (< (p 0) (p 1)) 1 0)))
         (reduce +))))

(println (solve (string/split-lines (slurp "input.txt"))))
