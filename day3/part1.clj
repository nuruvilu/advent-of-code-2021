
(require '[clojure.string :as string])

(defn get-gam-eps [pivoted-input gamma epsilon]
  (if (empty? pivoted-input)
    [gamma epsilon]
    (let [ones (count (filter #(= % \1) (first pivoted-input)))
          zeros (- (count (first pivoted-input)) ones)]
      (get-gam-eps
       (rest pivoted-input)
       (+ (bit-shift-left gamma 1) (if (> ones zeros) 1 0))
       (+ (bit-shift-left epsilon 1) (if (< ones zeros) 1 0))))))

(defn solve [input-list]
    (reduce * (get-gam-eps (apply map str input-list) 0 0)))

(println (solve (string/split-lines (slurp "input.txt"))))
