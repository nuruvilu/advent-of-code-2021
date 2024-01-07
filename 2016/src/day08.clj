(require '[clojure.string :as string])
(require '[clojure.set :as set])
(require '[clojure.math.combinatorics :as combo])

(def rect-regex #"rect (\d+)x(\d+)")
(def row-regex #"rotate row y=(\d+) by (\d+)")
(def col-regex #"rotate column x=(\d+) by (\d+)")

(defn parse-coords [[_ x-str y-str]]
  [(Integer/parseInt x-str) (Integer/parseInt y-str)])

(defn parse-instruction [instruction-text]
  (let [rect (re-matches rect-regex instruction-text)
        row (re-matches row-regex instruction-text)
        col (re-matches col-regex instruction-text)]
    (cond
      rect [:rect (parse-coords rect)]
      row [:row (parse-coords row)]
      col [:col (parse-coords col)])))

(defn parse [input]
  (->> (string/split-lines input)
       (map parse-instruction)))

(defn draw-rectangle [screen x y]
  (set/union screen
             (apply hash-set (combo/cartesian-product (range x) (range y)))))

(defn rotate-row [screen row dist width]
  (->> screen
       (map #(let [[x y] %]
               (if (= y row)
                 [(mod (+ x dist) width) y]
                 [x y])))
       (apply hash-set)))

(defn rotate-col [screen col dist height]
  (->> screen
       (map #(let [[x y] %]
               (if (= x col)
                 [x (mod (+ y dist) height)]
                 [x y])))
       (apply hash-set)))

(defn run-instruction [screen [width height] [instruction [n1 n2]]]
  (cond
    (= instruction :rect) (draw-rectangle screen n1 n2)
    (= instruction :row) (rotate-row screen n1 n2 width)
    (= instruction :col) (rotate-col screen n1 n2 height)))

(defn simulate-screen [instructions dimensions]
  (reduce #(run-instruction %1 dimensions %2) #{} instructions))

(defn print-screen [screen [width height]]
  (doseq [y (range height)
          x (range width)]
    (print (if (contains? screen [x y]) "#" "."))
    (when (= x (dec width)) (println "."))))

(defn part1 [input dimensions]
  (count (simulate-screen (parse input) dimensions)))

(defn part2 [input dimensions]
  (print-screen (simulate-screen (parse input) dimensions) dimensions))

(def sample (slurp "../samples/day08.txt"))
(assert (= (part1 sample [7 3]) 6))
(println "sample good")
(def input (slurp "../inputs/day08.txt"))
(println {:silver (part1 input [50 6]) :gold (part2 input [50 6])})
