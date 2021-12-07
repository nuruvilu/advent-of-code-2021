
(require '[clojure.string :as string])

(defn dist [x y] (if (> x y) (- x y) (- y x)))

(defn gauss [x] (/ (* x (inc x)) 2))

(defn solve [input-list]
    (->> (range (apply min input-list) (inc (apply max input-list)))
         (map #(reduce + (map (fn [x] (gauss (dist x %))) input-list)))
         (apply min)))

(println (solve (map #(Integer/parseInt %)
                     (string/split (slurp "input.txt") #","))))
