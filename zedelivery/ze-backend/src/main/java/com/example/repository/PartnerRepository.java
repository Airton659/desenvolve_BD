package com.example.repository;

import com.example.model.Partner;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PartnerRepository extends JpaRepository<Partner, String> {
    
}