
(require '[clojure.string :as string])

(defn solve [input-list]
  (->> (map #(string/trim (last (string/split % #"\|"))) input-list)
       (map #(string/split % #" "))
       (map #(count (filter (fn [s] (contains? #{2 3 4 7} (count s))) %)))
       (reduce +)))

(println (solve (string/split-lines (slurp "input.txt"))))
