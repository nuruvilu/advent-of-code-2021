(require '[clojure.string :as string])

(defn triangle? [[A B C]] (> (- (+ A B C) (max A B C)) (max A B C)))

(defn parse [input-text]
  (map #(map (fn [s] (Integer/parseInt s))
             (string/split (string/trim %) #"\s+"))
       (string/split-lines input-text)))

(defn rotate [[[A1 B1 C1] [A2 B2 C2] [A3 B3 C3]]]
  [[A1 A2 A3] [B1 B2 B3] [C1 C2 C3]])

(defn pivot [triangles] (mapcat rotate (partition 3 triangles)))

(defn part1 [input] (count (filter triangle? (parse input))))

(defn part2 [input] (count (filter triangle? (pivot (parse input)))))

(assert (not (triangle? [5 10 25])))

(def input (slurp "../inputs/day03.txt"))
(println {:silver (part1 input) :gold (part2 input)})
