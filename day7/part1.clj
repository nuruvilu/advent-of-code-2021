
(require '[clojure.string :as string])

(defn dist [x y] (if (> x y) (- x y) (- y x)))

(defn solve [input-list]
  (->> (range (apply min input-list) (inc (apply max input-list)))
        (map #(reduce + (map (fn [x] (dist x %)) input-list)))
        (apply min)))

(println (solve (map #(Integer/parseInt %)
                     (string/split (slurp "input.txt") #","))))
