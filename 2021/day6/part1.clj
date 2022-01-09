
(require '[clojure.string :as string])

(defn pad-fish [num fish-map]
  (if (= num 9)
    fish-map
    (pad-fish (inc num)
              (if (= (get fish-map num) nil)
                (merge fish-map {num 0})
                fish-map))))

(defn grow-fish [days-left fish]
  (if (= days-left 0)
    fish
    (grow-fish (dec days-left)
               (conj (vec (map + (rest fish) [0 0 0 0 0 0 (first fish) 0]))
                     (first fish)))))

(defn solve [input-list]
  (->> (map #(Integer/parseInt %) input-list)
       (frequencies)
       (pad-fish 0)
       (sort-by key)
       (vals)
       (grow-fish 80)
       (reduce +)))

(println (solve (string/split (slurp "input.txt") #",")))
