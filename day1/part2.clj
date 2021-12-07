
(require '[clojure.string :as string])

(defn to-int [string]
  (Integer/parseInt string))

(defn count-increases [nums]
  (->> (map vector nums (rest nums))
       (map (fn [p] (if (< (p 0) (p 1)) 1 0)))
       (reduce +)))

(defn solve [input-list]
  (let [inputs (map to-int input-list)]
    (->> (map vector inputs (rest inputs) (rest (rest inputs)))
         (map (fn [v] (apply + v)))
         (count-increases))))

(println (solve (string/split-lines (slurp "input.txt"))))
