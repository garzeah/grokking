var merge = function (intervals) {
  // Sorting by start time
  intervals.sort((a, b) => a[0] - b[0]);

  const mergedIntervals = [];
  let start = intervals[0][0];
  let end = intervals[0][1];

  for (let i = 1; i < intervals.length; i++) {
    const interval = intervals[i];

    // Overlapping intervals, determine the higher end time
    if (interval[0] <= end) end = Math.max(end, interval[1]);
    // Non-overlapping intervals, we push a new interval in
    else {
      mergedIntervals.push([start, end]);
      start = interval[0];
      end = interval[1];
    }
  }

  // Adding the last interval
  mergedIntervals.push([start, end]);
  return mergedIntervals;
};
