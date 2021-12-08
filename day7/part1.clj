
(require '[clojure.string :as string])

(defn solve [input-list]
  (->> (range (apply min input-list) (inc (apply max input-list)))
        (map #(reduce + (map (fn [x] (Math/abs (- x %))) input-list)))
        (apply min)))

(println (solve (map #(Integer/parseInt %)
                     (string/split (slurp "input.txt") #","))))
