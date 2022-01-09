
(require '[clojure.string :as string])

(defn to-int [string]
  (Integer/parseInt string))

(defn solve [input-list]
  (let [moves (map (fn [s] (string/split s #" ")) input-list)]
    (->> (filter (fn [move] (not= (move 0) "forward")) moves)
         (map (fn [move] (* (to-int (move 1)) (if (= (move 0) "down") 1 -1))))
         (map * (repeat
                 (->> moves
                      (filter (fn [move] (= (move 0) "forward")))
                      (map (fn [move] (to-int (move 1))))
                      (reduce +))))
         (reduce +))))
         
(println (solve (string/split-lines (slurp "input.txt"))))
