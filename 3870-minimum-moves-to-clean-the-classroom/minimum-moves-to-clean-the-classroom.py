from collections import deque
from typing import List


class Solution:

    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        start_r, start_c = -1, -1
        litter_coords = []

        # Find start position and all litter locations
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == "S":
                    start_r, start_c = r, c
                elif classroom[r][c] == "L":
                    litter_coords.append((r, c))

        num_litter = len(litter_coords)
        full_mask = (1 << num_litter) - 1

        # Map litter coordinates to bit index
        litter_map = {pos: i for i, pos in enumerate(litter_coords)}

        # Initial mask based on starting cell if it happens to be litter (rare)
        initial_mask = 0
        if (start_r, start_c) in litter_map:
            initial_mask |= 1 << litter_map[(start_r, start_c)]

        if initial_mask == full_mask:
            return 0

        # Queue stores: (row, col, mask, current_energy)
        queue = deque([(start_r, start_c, initial_mask, energy)])

        # Track maximum remaining energy for state (row, col, mask) to prune inefficient paths
        best_energy = {}
        best_energy[(start_r, start_c, initial_mask)] = energy

        steps = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            for _ in range(len(queue)):
                r, c, mask, e = queue.popleft()

                # If energy drops below required for another step, cannot proceed unless at 'R'
                if e == 0:
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Check grid boundaries and obstacles
                    if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != "X":
                        next_cell = classroom[nr][nc]
                        next_mask = mask
                        next_energy = e - 1

                        # Collect litter
                        if next_cell == "L" and (nr, nc) in litter_map:
                            next_mask |= 1 << litter_map[(nr, nc)]

                        # Check target state
                        if next_mask == full_mask:
                            return steps + 1

                        # Reset energy if on 'R'
                        if next_cell == "R":
                            next_energy = energy

                        state = (nr, nc, next_mask)

                        # Only push to queue if we reached this state with strictly more energy
                        if (
                            state not in best_energy
                            or next_energy > best_energy[state]
                        ):
                            best_energy[state] = next_energy
                            queue.append((nr, nc, next_mask, next_energy))

            steps += 1

        return -1